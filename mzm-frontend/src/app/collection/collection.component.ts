import { Component } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import 'rxjs/add/operator/switchMap';
import { DataService } from '../services/data.service'

@Component({
  selector: 'collection',
  providers: [
  ],
  styles: [ require('./collection.style.scss') ],
  templateUrl: './collection.template.html'
})
export class Collection {
  public collectionName: string;
  public collections: Array<any>;
  public currentPage: number;
  public totalPage: number;
  private limit: number;
  private offset: number;

  constructor(
    private route: ActivatedRoute,
    private dataService: DataService
  ){
    this.collectionName = "";
    this.limit = 20;
    this.offset = 0;
  }

  ngOnInit() {
    this.route.params
      .subscribe((params: Params) => {
        this.collectionName = params['collectionName'];
        this.getCollections(this.collectionName);
        console.log(this.collectionName);
      });
  }

  getCollections(collectionName: string): void {
    this.dataService
        .getCollections(collectionName, this.offset, this.limit)
        .then(data => {
          this.collections = data.result;
          this.currentPage = data.current;
          this.totalPage = data.total;
        });
  }

  setLimit(limit: number): void {
    this.limit = limit;
    this.offset = 0;
    this.getCollections(this.collectionName);
  }

  changePage(di: number): void {
    this.offset += di*this.limit;
    if(this.offset<0){
      this.offset = 0
    } else if (this.offset/this.limit > this.totalPage) {
      this.offset = this.totalPage * this.limit;
      this.currentPage -= 1;
    }
    this.getCollections(this.collectionName);
  }
}