import { Component } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {FormsModule} from "@angular/forms"
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Peergrade';
  public api_url = 'http://127.0.0.1:8000';
  get_data = function(){
    console.log(this.api_url);
    let data = null;
    this.http.get(this.api_url)
      .subscribe((response) => {
        data = response.json();
        console.log("API sent", data);
      });
  };

  onSubmit = function(my_form: any){
    this.post_data(my_form.value);
  };

  post_data = function (my_form) {
    this.http.post(this.api_url, my_form)
      .subscribe((response) => {
        console.log("POST API sent");
      });
  };
}
