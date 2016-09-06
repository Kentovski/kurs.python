import {Component, OnInit} from '@angular/core';
import {HttpService} from './app.service';
import {ROUTER_DIRECTIVES} from '@angular/router';


@Component({
    template: `
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    <h4 class="text-muted">Все выполенные задания:</h4>
                    <table class="table">
                        <thead>
                          <tr>
                            <th>Номер </th>
                            <th>Запрос</th>
                            <th>Яндекс, шт</th>
                            <th>Google, шт</th>
                            <th>Instagram, шт</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr *ngFor="let task of tasks">
                            <td>{{ task.id }}</td>
                            <td><a [routerLink]="['/task', task.id]">{{ task.query }}</a></td>
                            <td>{{ task.yandex }}</td>
                            <td>{{ task.google }}</td>
                            <td>{{ task.instagram }}</td>
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
export class TasksComponent implements OnInit{
    tasks: any[];

    constructor(private _httpservice: HttpService){}

    ngOnInit(){
        this._httpservice.getTasks()
            .subscribe((data) => this.tasks = data.json())
    }

}