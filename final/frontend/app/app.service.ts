import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/observable/interval';

@Injectable()
export class HttpService {
    constructor(private _http: Http){}

    getStatus(task_id: string) {
        return Observable
        .interval(2500)
        .flatMap(() => {
            return this._http.get(`https://agregator-1995e.firebaseio.com/results.json?task-id=${task_id}`)
        });
    }

    sendRequest(query: string){
        return this._http.get(`http://httpbin.org/ip?query=${query}`);
    }

    getTotalStats(){
        return this._http.get(`https://agregator-1995e.firebaseio.com/totalstats.json`);
    }

    getTasks(){
        return this._http.get(`https://agregator-1995e.firebaseio.com/tasks.json`);
    }

    getTask(id: string){
        return this._http.get(`https://agregator-1995e.firebaseio.com/task.json?id=${id}`);
    }
}