/* ID: 5a2e9ae2b6cfd7692a0000ba

Return the type of the sum of the two arguments */

function typeOfSum(a, b) {
  return typeof a === "string" || typeof b === "string" ? "string" : "number";
}
