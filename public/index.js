
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
    get onLoad() {
        fetch("/data/rankings.json")
        .then(res => res.json())
        .then(products => {
            this.fighters = products;
            this.allFighters = products;
            this.searchFighters = products;
        })
    },
    onChange() {
        let tempFighters = [];
        for (let fighter of this.searchFighters) {
            if (fighter.name.toLowerCase().includes(this.search.toLowerCase())){
                tempFighters.push(fighter);
            }
        }
        this.fighters = tempFighters;
    }, 
    onWeightChange(weightClass) {
        let tempFighters = [];
        this.fighters = [];
        if (weightClass != 'all') {
            
            tempFighters = [];
            if (weightClass == 'men'){
                let i = 1;
                for (let fighter of this.allFighters) {
                    if (!fighter.weight.includes("Women's Featherweight") &&
                        !fighter.weight.includes("Women's Batamweight") &&
                        !fighter.weight.includes("Women's Flyweight") &&
                        !fighter.weight.includes("Women's Strawweight"))
                    {
                        fighter.rank = i;
                        tempFighters.push(fighter)
                        i += 1;
                    }
                }
                weightClass = "All Men" 
            } else if (weightClass == 'women'){
                let i = 1;
                for (let fighter of this.allFighters) {
                    if (fighter.weight.includes("Women's Featherweight") ||
                        fighter.weight.includes("Women's Batamweight") ||
                        fighter.weight.includes("Women's Flyweight") ||
                        fighter.weight.includes("Women's Strawweight"))
                    {
                        fighter.rank = i;
                        tempFighters.push(fighter)
                        i += 1;
                    }
                }
                weightClass = "All Women" 
            } else {
                let i = 1;
                for (let fighter of this.allFighters) {
                    if (fighter.weight.includes(weightClass)){
                        fighter.rank = i;
                        tempFighters.push(fighter)
                        i += 1;
                    }
                }
            }
            this.fighters = tempFighters;
            this.searchFighters = tempFighters;
            this.weight = weightClass;
        } else {
            this.fighters = this.allFighters;
            this.searchFighters = this.allFighters;
            this.weight = "All Fighters";
        }
        
    }
    
}).mount("#body");


