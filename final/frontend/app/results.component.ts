import {Component} from '@angular/core';
import {ROUTER_DIRECTIVES} from '@angular/router';

@Component({
    selector: 'results',
    template: `
        <div class="row">
            <div class="col-sm-12">
                <div class="alert alert-info">
                  Полная информация по этому заданию доступна по этой 
                  <a [routerLink]="['task', task_id]"><strong>ссылке</strong></a> 
                </div>
                <div>
                    <a *ngFor="let image of results.yandex" [href]="image.direct_link" target="_blank">
                        <img [src]="image.direct_link" title="Открыть в новой вкладке" >
                        <img [src]="yandex_icon" icon>
                    </a>
                    <a *ngFor="let image of results.instagram" [href]="image.direct_link" target="_blank">
                        <img [src]="image.direct_link" title="Открыть в новой вкладке" >
                        <img [src]="instagram_icon" icon>
                    </a>
                    <a *ngFor="let image of results.google" [href]="image.direct_link" target="_blank">
                        <img [src]="image.direct_link" title="Открыть в новой вкладке" >
                        <img [src]="google_icon" icon>
                    </a>
                </div>
            </div>
        </div>
    `,
    styles: [`
        img[title]{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 10px auto;
        }
        img[icon]{
            position: relative;
            top: -45px;
            left: -150px;
        }
    `],
    inputs: ['results', 'task_id'],
    directives: [ROUTER_DIRECTIVES, ]
})
export class ResultsComponent{
    google_icon = "../img/google.png"
    yandex_icon = "../img/yandex.png"
    instagram_icon = "../img/instagram.png"
}
