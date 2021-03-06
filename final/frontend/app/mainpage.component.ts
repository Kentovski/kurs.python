import {Component, OnInit} from '@angular/core';
import {HttpService} from './app.service';
import {Data} from './data.interface.ts';
import {TotalStatsComponent} from './totalstats.component';
import {CrawlingStateComponent} from './crawlingstate.component';
import {ResultsComponent} from './results.component';

@Component({
  templateUrl: 'app/mainpage.component.html',
  providers: [HttpService, ],
  directives: [TotalStatsComponent, CrawlingStateComponent, ResultsComponent]
})
export class MainPageComponent  {
    task_id: string;
    query: string;
    data: Data;
    isCrawling: boolean = false;
    isFihished: boolean = false;

    constructor(private _httpService: HttpService){}

    onCrawl(){
        this._httpService.sendRequest(this.query)
            .subscribe(result => {
                this.isCrawling = true;
                let res = result.json();
                this.task_id = res['task_id']
                let tasksSubscription = this._httpService.getStatus(this.task_id)
                .subscribe(
                        (data) => {
                            this.data = data.json();
                            console.log(this.data);
                            if (this.data['results']){
                                this.isCrawling = false;
                                this.isFihished = true;
                                tasksSubscription.unsubscribe();
                            }
                        }
                    )
                },
                (error) => console.log(error)
            );
    }

}