export default function FlexHeader() {
  let headers = [
    "Features",
    "Equipment",
    "Proficiencies",
    "Spells",
    "Power Attack",
    "Flavor"
  ];

  let ret = [];

  headers.forEach(element => {
    let  lower = element.replace(" ", "").toLowerCase()

    ret.push(
      <button
        type="button"
        id={lower+"Button"}
        key={lower+"TabHeader"}
        className="tabButton"
        data-for-tab={"main-"+lower}
      >
        {element}
      </button>
    );
  });

  return (
    <div className="flexHeader tabHeader">
      {ret}
    </div>
  );
}
