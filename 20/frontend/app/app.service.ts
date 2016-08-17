import {Http, URLSearchParams} from '@angular/http';
import { Injectable }     from '@angular/core';
import 'rxjs/add/operator/map'
import {InitData} from './initData'

@Injectable()
export class AppService{
    constructor(private _http: Http){}

    getResult(battle: InitData){
        return this._http.get(`http://127.0.0.1:5000?armies=${battle.armies}&squads=${battle.squads}&vehicles=${battle.vehicles}&solders=${battle.solders}`)
            .map(res => res.text())
    }
}