import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/observable/interval';

@Injectable()
export class HttpService {
    constructor(private _http: Http){}

    getStatus(task_id: string) {
        return Observable
        .interval(1000)
        .flatMap(() => {
            return this._http.get(`http://127.0.0.1:8000/send-status/?task-id=${task_id}`)
        });
    }

    sendRequest(query: string){
        return this._http.get(`http://127.0.0.1:8000/get-request/?query=${query}`);
    }

    getTotalStats(){
        return this._http.get(`http://127.0.0.1:8000/send-total-stats/`);
    }

    getTasks(){
        return this._http.get(`http://127.0.0.1:8000/send-tasks`);
    }

    getTask(id: string){
        return this._http.get(`http://127.0.0.1:8000/send-task/?id=${id}`);
    }
}