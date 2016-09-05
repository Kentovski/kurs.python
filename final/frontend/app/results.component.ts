import {Component} from '@angular/core';

@Component({
    selector: 'results',
    template: `
        <div class="row">
            <div class="col-sm-12">
            <div>
                <a *ngFor="let image of results.yandex" [href]="image.direct_link" target="_blank">
                    <img [src]="image.direct_link" [title]="'#: ' + image.rank" >
                    <img [src]="yandex_icon" icon>
                </a>
                <a *ngFor="let image of results.instagram" [href]="image.direct_link" target="_blank">
                    <img [src]="image.direct_link" [title]="'#: ' + image.rank" >
                    <img [src]="instagram_icon" icon>
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
        }
        img[icon]{
            position: relative;
            top: -45px;
            left: -150px;
        }
    `],
    inputs: ['results']
})
export class ResultsComponent{
    google_icon = "../img/google.png"
    yandex_icon = "../img/yandex.png"
    instagram_icon = "../img/instagram.png"


}
