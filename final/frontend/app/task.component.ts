import {Component, OnInit} from '@angular/core';
import {ROUTER_DIRECTIVES, ActivatedRoute} from '@angular/router';

import {HttpService} from './app.service';

@Component({
    template: `
        <div class="container">
            <div class="row">
                <div class="col-sm-12" *ngIf="!isLoading">
                    <h4 class="text-muted">Статистика по заданию № {{ id }}</h4>
                    <div *ngIf="isLoading">
                        <i class="fa fa-spinner fa-spin fa-3x"></i>
                    </div>
                    <table class="table" *ngIf="!isLoading">
                        <thead>
                          <tr>
                            <th>Прямая ссылка</th>
                            <th>Источник</th>
                            <th>Откуда спарсена</th>
                            <th>Позиция</th>
                            <th>Когда спарсена</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr *ngFor="let task of task_data">
                            <td><a [href]="task.direct_link" target="_blank">Перейти</a></td>
                            <td><a [href]="task.source_link" target="_blank">Перейти</a></td>
                            <td [ngSwitch]="task.site">
                                <span *ngSwitchCase="'y'">Яндекс</span>
                                <span *ngSwitchCase="'g'">Гугл</span>
                                <span *ngSwitchCase="'i'">Инстаграм</span>
                            </td>
                            <td>{{ task.rank }}</td>
                            <td>{{ task.date }}</td>
                          </tr>
                        </tbody>
                      </table>
                </div>
            </div>
        </div>
    `,
    directives: [ROUTER_DIRECTIVES],
    providers: [HttpService]
})
export class TaskComponent implements OnInit{
    isLoading: boolean = true;
    id: string;
    task_data;

    constructor(private _activatedRoute: ActivatedRoute, private _httpservice: HttpService){
        this.id = _activatedRoute.snapshot.params['id']
    }

    ngOnInit(){
        this._httpservice.getTask(this.id)
            .subscribe((data) => {
                this.isLoading = false;
                this.task_data = data.json()
            })
    }

}