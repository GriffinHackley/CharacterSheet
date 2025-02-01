export default function formatSource(sources) {
  let first = true;
  let fullString = "";

  for (let source in sources) {
    let value = sources[source];
    let string = "";
    if (first) {
      first = false;
      string = value.toString() + "(" + source + ")";
    } else {
      if (typeof value == "number" && value < 0) {
        value = value.toString().split("-")[1];
        string = " - " + value + "(" + source + ")";
      } else if (typeof value === "number" && value === 0) {
      } else {
        string = " + " + value.toString() + "(" + source + ")";
      }
    }
    fullString += string;
  }

  return fullString;
}
