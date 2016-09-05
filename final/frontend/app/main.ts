import {bootstrap} from '@angular/platform-browser-dynamic';
import {enableProdMode} from '@angular/core';
import {provideForms, disableDeprecatedForms} from '@angular/forms';
import {HTTP_PROVIDERS} from '@angular/http';

import {AppComponent} from './app.component';
import {APP_ROUTES_PROVIDER} from './app.routes';

// enableProdMode();

bootstrap(AppComponent, [disableDeprecatedForms(), provideForms(), HTTP_PROVIDERS, APP_ROUTES_PROVIDER]);