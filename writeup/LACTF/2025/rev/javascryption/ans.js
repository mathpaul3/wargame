function getFlag() {
  const str =
    "JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I=";
  const step5 = atob(str);
  const step4 = decodeURIComponent(step5);
  const step3 = step4.replaceAll("[OLD_DATA]", "Z");
  const step2 = step3.split("").reverse().join("");
  const step1 = atob(step2);
  return step1;
}

console.log(getFlag());
