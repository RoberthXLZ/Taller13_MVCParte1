import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ApiService } from './api.service';
import { CrearReciboComponent } from './crear-recibo/crear-recibo.component';
import { EditarReciboComponent } from './editar-recibo/editar-recibo.component';

@NgModule({
  declarations: [
    AppComponent,
    CrearReciboComponent,
    EditarReciboComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
