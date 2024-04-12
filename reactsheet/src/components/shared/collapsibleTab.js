import { useState } from "react";

function getContent(content, expanded) {
  if (expanded) {
    let text = [];
    content.forEach(line => {
      if (line.type == "normal") {
        text.push(
          <p>
            {line.text}
          </p>
        );
      } else if (line.type == "heading") {
        text.push(
          <h4>
            {line.text}
          </h4>
        );
      } else if (line.type == "table") {
        <h1>Tables have not been implemented</h1>;
      }
    });
    return (
      <div>
        {text}
      </div>
    );
  } else {
    return;
  }
}

export default function CollapsibleTabs({ name, text }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="feature">
      <button
        type="button"
        className="featureName collapsible"
        key={name}
        onClick={() => setExpanded(!expanded)}
      >
        {name}
      </button>
      <div className="featureDescription">
        {getContent(text, expanded)}
      </div>
    </div>
  );
}
