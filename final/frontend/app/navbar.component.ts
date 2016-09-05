import {Component} from '@angular/core';
import {ROUTER_DIRECTIVES} from '@angular/router';

@Component({
    selector: 'navbar',
    template: `
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
             <a [routerLink]="['']" class="navbar-brand">Агрегатор картинок</a>
        </div>
        <ul class="nav navbar-nav">
          <li><a [routerLink]="['']">Главная</a></li>
          <li><a [routerLink]="['tasks']">Задания</a></li>
        </ul>
      </div>
    </nav>
    `,
    directives: [ROUTER_DIRECTIVES]
})
export class NavbarComponent{}