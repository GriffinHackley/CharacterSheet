import { useState } from "react";
import "../../css/shared/CollapsibleTab.css";

export default function CollapsibleTab({ name, text }) {
  const [expanded, setExpanded] = useState(false);

  let description = null;
  if (expanded) {
    description = (
      <div
        className="featureDescription"
        dangerouslySetInnerHTML={{ __html: text }}
      />
    );
  }

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
      {description}
    </div>
  );
}
