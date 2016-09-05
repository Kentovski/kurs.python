import {Component, Input} from '@angular/core';
import {HttpService} from './app.service';
import {Data} from './data.interface.ts';
import {StatusIconComponent} from './statusicon.component';


@Component({
    selector: 'crawling-state',
    template: `
        <div class="row" *ngIf="isCrawling && data">
                <div class="col-sm-3">
                    <ul class="list-group">
                      <li class="list-group-item borderless">Google <status-icon [status]="data?.spiders?.google"></status-icon></li>
                      <li class="list-group-item borderless">Yandex <status-icon [status]="data?.spiders?.yandex"></status-icon></li> 
                      <li class="list-group-item borderless">Instagram <status-icon [status]="data?.spiders?.instagram"></status-icon></li> 
                    </ul>
                </div>
            </div>
    `,
    styles: [`.borderless {border: none}`],
    directives: [StatusIconComponent, ]
})
export class CrawlingStateComponent {
    @Input() isCrawling;
    @Input() data: Data;
}