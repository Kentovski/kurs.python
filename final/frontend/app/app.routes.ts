import {MainPageComponent} from './mainpage.component';
import {TaskComponent} from './task.component';
import {TasksComponent} from './tasks.component';
import {provideRouter} from '@angular/router';

const APP_ROUTES = [
    {path: '', component: MainPageComponent},
    {path: 'task/:id', component: TaskComponent},
    {path: 'tasks', component: TasksComponent},
    {path: '**', redirectTo: ''},
];

export const APP_ROUTES_PROVIDER = [
    provideRouter(APP_ROUTES)
];