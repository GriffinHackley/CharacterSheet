import "../../css/pages/Flavor.css";
import { useLocation } from "react-router-dom";

export default function Flavor() {
  const location = useLocation();
  const { flavorInfo } = location.state;

  let mainHeader = "backstory";
  let main = [];
  let columnContainer = [];

  for (let header in flavorInfo) {
    //Capitalize Header
    let headerText = header.charAt(0).toUpperCase() + header.slice(1);
    if (headerText == "PersonalityTraits") {
      headerText = "Personality Traits";
    }

    let content = [];
    let contentText = flavorInfo[header];
    contentText = contentText.split("\n");
    for (let line in contentText) {
      content.push(
        <p>
          {contentText[line]}
        </p>
      );
    }

    if (mainHeader == header) {
      main.push(
        <div className={"main " + header}>
          <h2>
            {headerText}
          </h2>
          {content}
        </div>
      );
    } else {
      columnContainer.push(
        <div className={header}>
          <h2>
            {headerText}
          </h2>
          <div className="flavorText">
            {content}
          </div>
        </div>
      );
    }
  }

  return (
    <section class="flavor">
      {main}
      <div class="columnContainer">
        {columnContainer}
      </div>
    </section>
  );
}
