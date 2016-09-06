from django.http import JsonResponse
from django.views.decorators.http import require_GET

from rest_framework.renderers import JSONRenderer
from agregator.models import Tasks, Results
from agregator.serializers import ResultsSerializer, TaskSerializer
import requests
import json


@require_GET
def get_request(request):
    if 'query' in request.GET and request.GET.get('query', ''):
        query = request.GET['query']
        task = Tasks(query=query)
        task.save()
        spiders_response = {}
        for spider in ['google', 'yandex', 'instagram']:
            response = requests.post(
                'http://localhost:6800/schedule.json',
                data={
                    'project': 'parsers',
                    'spider': spider,
                    'django_task_id': task.id,
                    'query': query,
                    'pages': 2
                })
            spiders_response[spider] = response.json()
        t = Tasks.objects.get(id=task.id)
        t.scrapyd_response = spiders_response
        t.save()
        return JsonResponse({'task_id': t.id})
    return JsonResponse({'error': 'Invalid query string'})


@require_GET
def send_status(request):
    if 'task-id' in request.GET and request.GET.get('task-id', ''):

        # Get each scrapyd's crawler from base
        task_id = request.GET['task-id']
        task = Tasks.objects.get(id=task_id)
        task_crawlers = {}
        scrapyd = json.loads(task.scrapyd_response.replace("'", '"'))
        for spider, info in scrapyd.items():
            task_crawlers[spider] = info['jobid']

        # Ask scrapyd's state
        response = requests.get(
            'http://localhost:6800/listjobs.json?project=parsers'
            )
        scrapyd_response = response.json()

        # Check response from scrapyd
        if 'running' not in scrapyd_response:
            # If key 'running' not exists in scrapyd response
            return JsonResponse({'errors': 'Can not get data from scrapid.', 'results': ''})
        spiders = {}
        if not scrapyd_response.get('running') and not scrapyd_response.get('pending'):
            results = {}
            for site in ['google', 'yandex', 'instagram']:
                r = Results.objects.filter(site=site[0]).order_by('rank')
                results[site] = ResultsSerializer(r, many=True).data
            return JsonResponse({
                "errors": '',
                "spiders": {
                    "google": "finished",
                    "yandex": "finished",
                    "instagram": "finished"
                },
                "results": results
                })
            # Crawling finished. Get results from base
        else:
            # On crawling. Return crawler's state
            for spider, id in task_crawlers.items():
                for status in ['finished', 'running', 'pending']:
                    for i in scrapyd_response.get(status):
                        if i['id'] == id:
                            spiders[spider] = status

            return JsonResponse({'errors': '', 'spiders': spiders, 'results': ''})

    return JsonResponse({'errors': 'You should send valid task id'})


@require_GET
def send_task(request):
    if 'id' in request.GET and request.GET.get('id', ''):
        task_id = request.GET['id']
        queryset = Results.objects.filter(task__id=task_id)
        serialized = TaskSerializer(queryset, many=True)
        return JsonResponse(serialized.data, safe=False)

    return JsonResponse({'errors': 'Invalid task id'})


@require_GET
def send_tasks(request):
    tasks = Tasks.objects.all()
    res = []
    for task in tasks:
        r = {}
        r['id'] = task.id
        r['query'] = task.query
        r['google'] = Results.objects.filter(task__id=task.id, site='g').count()
        r['yandex'] = Results.objects.filter(task__id=task.id, site='y').count()
        r['instagram'] = Results.objects.filter(task__id=task.id, site='i').count()
        res.append(r)
    return JsonResponse(res, safe=False)


@require_GET
def send_total_stats(request):
    res = {}
    res['google'] = Results.objects.filter(site='g').count()
    res['yandex'] = Results.objects.filter(site='y').count()
    res['instagram'] = Results.objects.filter(site='i').count()
    return JsonResponse(res)
