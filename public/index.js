
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDnYM6AbGp27J-u2r5nLL9Ie0oZTmsfrqk",
    authDomain: "mma-stats-38214.firebaseapp.com",
    projectId: "mma-stats-38214",
    storageBucket: "mma-stats-38214.appspot.com",
    messagingSenderId: "73526909394",
    appId: "1:73526909394:web:5a14feb4e6eedb2dac900b",
    measurementId: "G-C29SR87P52"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

PetiteVue.createApp({
    search: '',
    weight: 'All Fighters',
    fighters: [],
    allFighters: [],
    searchFighters: [],
    weightSelect: "",
    page: 1,
    pageLimit: 50,
    totalPages: 1,
    visiblePageLimit: 12,
    get onLoad() {
        fetch("/data/rankings.json")
        .then(res => res.json())
        .then(products => {
            let i = 1;
            for (let product of products) {
                if (i <= this.pageLimit) {
                    this.fighters.push(product);
                } else {
                    break;
                }
                i += 1;
            }
            this.allFighters = products;
            this.searchFighters = products;
            this.updateTotalPages();
        })
    }, 
    updateTotalPages() {
        let len = this.searchFighters.length;
        let pages = Math.ceil(len / this.pageLimit);
        this.totalPages = pages;
        if (this.totalPages > 12){
            this.visiblePageLimit = 12;
        } else {
            this.visiblePageLimit = this.totalPages;
        }

    },
    onChange() {
        let tempFighters = [];
        this.page = 1;
        let i = 1;
        for (let fighter of this.searchFighters) {
            if (fighter.name.toLowerCase().includes(this.search.toLowerCase())){
                if (i <= this.pageLimit) {
                    tempFighters.push(fighter);
                    i += 1;
                } else {
                    break;
                }
            }
        }
        if (this.search == "") {
            this.updateTotalPages();
        } else {
            this.totalPages = 1;
        }
        this.fighters = tempFighters;
    }, 
    changePage(newPage) {
        this.page = newPage;
        let i = this.page - 1;
        i = i * this.pageLimit;
        i += 1;
        let limit = i + this.pageLimit;
        let tempFighters = [];
        this.fighters = [];
        while (i < ( limit ) && i <= this.searchFighters.length){
            let tempFighter = this.searchFighters[i - 1];
            tempFighters.push(tempFighter);
            i += 1;
        }
        this.fighters = tempFighters;
    },
    nextLastPage(change) {
        let newPage = this.page;
        if (change == 'next' && this.page < this.totalPages) {
            newPage += 1;
        } else if (change == 'last' && this.page > 1) {
            newPage -= 1;
        } else if (change == 'start') {
            newPage = 1;
        } else if (change == 'end') {
            newPage = this.totalPages;
        }
        this.changePage(newPage);
    },
    onWeightChange(weightClass) {
        this.page = 1;
        let tempFighters = [];
        let fighterLimit = [];
        this.fighters = [];
        this.searchFighters = [];
        let i = this.page - 1;
        i = i * this.pageLimit;
        i += 1;
        if (weightClass != 'all') {
            
            tempFighters = [];
            if (weightClass == 'men'){
                for (let fighter of this.allFighters) {
                    if (!("Women's Featherweight" in fighter.weight) &&
                        !("Women's Batamweight" in fighter.weight) &&
                        !("Women's Flyweight" in fighter.weight) &&
                        !("Women's Strawweight" in fighter.weight))
                    {
                        let tempFighter = fighter;
                        tempFighter.rank = i;
                        tempFighters.push(tempFighter);
                        if (i <= (this.pageLimit * this.page)) {
                            fighterLimit.push(tempFighter);
                        }
                        i += 1;
                    }
                }
                weightClass = "All Men" 
            } else if (weightClass == 'women'){
                for (let fighter of this.allFighters) {
                    if (("Women's Featherweight" in fighter.weight) ||
                        ("Women's Batamweight" in fighter.weight) ||
                        ("Women's Flyweight" in fighter.weight) ||
                        ("Women's Strawweight" in fighter.weight))
                    {
                        let tempFighter = fighter;
                        tempFighter.rank = i;
                        tempFighters.push(tempFighter);
                        if (i <= (this.pageLimit * this.page)) {
                            fighterLimit.push(tempFighter);
                        }
                        i += 1;
                    }
                }
                weightClass = "All Women" 
            } else {
                for (let fighter of this.allFighters) {
                    if (weightClass in fighter.weight){
                        if (fighter.weight[weightClass] >= 3) {
                            let tempFighter = fighter;
                            tempFighter.rank = i;
                            tempFighters.push(tempFighter);
                            if (i <= (this.pageLimit * this.page)) {
                                fighterLimit.push(tempFighter);
                            }
                            i += 1;
                        }
                        
                    }
                }
            }
            this.fighters = fighterLimit;
            this.searchFighters = tempFighters;
            this.weight = weightClass;
        } else {

            for (let fighter of this.allFighters) {
                let tempFighter = fighter;
                tempFighter.rank = i;
                tempFighters.push(tempFighter);
                if (i <= (this.pageLimit * this.page)) {
                    fighterLimit.push(tempFighter);
                }
                i += 1;
            }
            this.fighters = fighterLimit;
            this.searchFighters = tempFighters;
            this.weight = "All Fighters";
        }
        this.updateTotalPages();
    }
    
}).mount("#body");


