import {Component} from '@angular/core';
import {AppService} from './app.service'
import {HTTP_PROVIDERS} from '@angular/http'


@Component({
    selector: 'my-app',
    templateUrl: 'app/app.component.html',
    providers: [AppService, HTTP_PROVIDERS]
})
export class AppComponent {
    isLoading  = true;
    result: string;

    constructor(private _appService: AppService){}

    start(form){
         this._appService.getResult(form.value).subscribe(res => {
             this.isLoading  = false;
             this.result = res;
         })
    }

}