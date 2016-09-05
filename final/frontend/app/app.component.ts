import {Component} from '@angular/core';
import {ROUTER_DIRECTIVES} from '@angular/router';

import {TasksComponent} from './tasks.component';
import {TaskComponent} from './task.component';
import {MainPageComponent} from './mainpage.component';
import {NavbarComponent} from './navbar.component';


@Component({
  selector: 'my-app',
  template: `
  <navbar></navbar>
  <router-outlet></router-outlet>
  `,
  directives: [ROUTER_DIRECTIVES, NavbarComponent],
  precompile: [MainPageComponent, TasksComponent, TaskComponent, NavbarComponent]
})
export class AppComponent  {}