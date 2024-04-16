import { useState } from "react";

function getContent(content, expanded) {
  if (expanded) {
    return content;
  } else {
    return;
  }
}

export default function CollapsibleTab({ name, text }) {
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
      <div
        className="featureDescription"
        dangerouslySetInnerHTML={{ __html: getContent(text, expanded) }}
      />
    </div>
  );
}
