import {Component, Input, OnInit} from '@angular/core';
import {HttpService} from './app.service';
import {TotalStats} from './totalstats.interface.ts';

@Component({
    selector: 'total-stats',
    template: `
        <div class="row" *ngIf="!isCrawling && !isFihished">
            <div class="col-sm-12" >
                <h4 class="text-muted">Общая статистика количества спарсенных картинок:</h4>
                <table class="table" >
                    <thead>
                      <tr>
                        <th>Google Images</th>
                        <th>Yandex Images</th>
                        <th>Instagram</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>{{ totalstats?.google }}</td>
                        <td>{{ totalstats?.yandex }}</td>
                        <td>{{ totalstats?.instagram }}</td>
                      </tr>
                    </tbody>
                  </table>
            </div>
        </div>
    `,
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