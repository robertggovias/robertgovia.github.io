let daynames = [
	"Sunday",
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday",
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	
];
let months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
];
let d = new Date();
let dayName = daynames[d.getDay()];
let monthName = months[d.getMonth()];
let year = d.getFullYear();
let hour = d.getHours();
let minutes = d.getMinutes();
let seconds = d.getSeconds();
let fulldate = dayName + ", " + monthName + " " + d.getDate() + ", " + year;
document.getElementById("currentdate").textContent = fulldate;
if(d.getDay()==5){document.getElementById("announce").textContent = "Saturday at 9:00 a.m. Preston Pancakes in the Park! at the city park pavilion."};
var ddd, ddn, dd;
ddn = 0;
for (dd = 0; dd < 12; dd++) {
	if (hour > 18) {
		ddd = "d" + ddn;
		document.getElementById(ddd).textContent = daynames[d.getDay() + dd + 1];
		ddn += 1;
	} else {
		ddd = "d" + ddn;
		document.getElementById(ddd).textContent = daynames[d.getDay() + dd];
		ddn += 1;
	}
}
//
    
// ****************************
let options = {
	weekday: 'long',
	day: 'numeric',
	month: 'long',
	year: 'numeric'
};
