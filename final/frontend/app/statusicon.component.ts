import {Component} from '@angular/core';

@Component({
    selector: 'status-icon',
    template: `
        <span [ngSwitch]="status">
            <i *ngSwitchCase="'running'" class="fa fa-spinner fa-spin" style="float:right"></i>
            <i *ngSwitchCase="'finished'" class="fa fa-check" style="color: green; float:right"></i>
            <i *ngSwitchCase="'pending'" class="fa fa-clock-o" style="float:right"></i>
        </span>
    `,
    inputs: ['status']
})
export class StatusIconComponent{}