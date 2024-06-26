
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
    fighters: [],
    allFighters: [],
    weightSelect: "",
    get onLoad() {
        fetch("/data/rankings.json")
        .then(res => res.json())
        .then(products => {
            this.fighters = products;
            this.allFighters = products;
        })
    },
    onChange(weightClass) {
        let tempFighters = [];
        for (let fighter of this.allFighters) {
            if (fighter.name.toLowerCase().includes(this.search.toLowerCase())){
                tempFighters.push(fighter);
            }
        }
        if (weightClass != '') {
            let newTempFighters = tempFighters;
            tempFighters = [];
            for (let fighter of newTempFighters) {
                if (fighter.weight.includes(weightClass)){
                    tempFighters.push(fighter)
                }
            }
        }
        this.fighters = tempFighters;
    }, 
    onWeightChange(weightClass) {
        console.log(weightClass);
        this.onChange(weightClass);
    }
    
}).mount("#body");


