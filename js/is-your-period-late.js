/* ID: 578a8a01e9fd1549e50001f1

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days


Return true if the number of days passed from last to today is greater than
cycleLength. Otherwise, return false. */

function periodIsLate(last, today, cycleLength) {
    last = new Date(last);
    today = new Date(today);
    if ((today.getTime() - last.getTime()) / (1000 * 3600 * 24) <= cycleLength) {
        return false;
    }
    return true;
}

// console.log(periodIsLate(2016-07-12, 2016-08-09, 28));