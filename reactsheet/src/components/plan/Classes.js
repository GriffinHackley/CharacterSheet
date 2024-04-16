function getFeatureTabs(contents) {
  let tabContents = [];
  //   for (let index in contents) {
  //     let feature = contents[index];

  //     tabContents.push(
  //       <div className="feature">
  //         <button
  //           type="button"
  //           className="featureName collapsible"
  //           key={feature.name}
  //           onClick={() => toggleExpanded(index)}
  //         >
  //           {feature.name}
  //         </button>
  //         <div className="featureDescription">
  //           {getContent(feature, expandedFeatures, index)}
  //         </div>
  //       </div>
  //     );
  //   }
  return tabContents;
}
export default function Classes({ classes }) {
  let content = {};
  let features = getFeatureTabs(content);
  return (
    <div>
      <h3>Classes</h3>
      {features}
    </div>
  );
}
