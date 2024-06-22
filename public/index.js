
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
    
    onChange() {
        update_list(this.search);
    }
    
}).mount("#body");

let data = [];
fetch("../rank_generator/rank_data/rankings.json")
.then(function(res){
    return res.json();
})
.then(function(products){
    data = products;
    update_list('');
})
    
function update_list(filter_string) {
    let placeholder = document.querySelector("#table-body-0");
    let out = "";
    let filtered_data = data;
    for(let product of filtered_data){
        if (product.name.toLowerCase().includes(filter_string.toLowerCase()) || filter_string == '') {
            out += `
            <tr>
                <td>${product.rank}</td>
                <td>${product.name}</td>
                <td>${product.rating}</td>
            </tr>
            `;
        }
    }
    placeholder.innerHTML = out;
}
