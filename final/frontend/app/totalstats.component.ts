import {Component, Input, OnInit} from '@angular/core';
import {HttpService} from './app.service';
import {TotalStats} from './totalstats.interface.ts';

@Component({
    selector: 'total-stats',
    template: `
        <div class="row" *ngIf="!isCrawling && !isFihished">
            <div class="col-sm-12" >
                <h4 class="text-muted text-center">Количество спарсенных ссылок в базе:</h4>
                <div class="row">
                    <div class="col-sm-4 text-center"><img src="../img/google-big.png"><h2>{{totalstats?.google}}</h2></div>
                    <div class="col-sm-4 text-center"><img src="../img/yandex-big.png"><h2>{{totalstats?.yandex}}</h2></div>
                    <div class="col-sm-4 text-center"><img src="../img/instagram-big.png"><h2>{{totalstats?.instagram}}</h2></div>
                </div>
            </div>
        </div>
    `,
    styles: [`
        .text-muted{
            margin-bottom: 30px;
        }
        h2{
            font-weight: bold;
        }
    `]
})
export class TotalStatsComponent implements OnInit{
    @Input() isCrawling;
    @Input() isFihished;
    totalstats: TotalStats;

    constructor(private _httpService: HttpService){}

    ngOnInit(){
        this._httpService.getTotalStats()
            .subscribe(result => this.totalstats = result.json())
    }
}