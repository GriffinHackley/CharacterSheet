export default function FeaturesTab({ featuresInfo }) {
  features = [];

  featuresInfo.forEach(element => {
    <button
      type="button"
      id={element.name + "Button"}
      class="tabButton"
      data-for-tab="feature-{{ featureType }}"
    >
      {element.featureType }
    </button>;
  });

  return (
    <div class="tabContent" data-tab="main-features">

    </div>
  )

  // return (
  //     <div class="tabContent" data-tab="main-features">
  //     <section class="features">
  //       <div class="featureHeader tabHeader">
  //         {% for featureType in character.features %}

  //         {% endfor %}
  //       </div>
  //       {% for featureType,features in character.features.items %}
  //         <div class="featureType tabContent" data-tab="feature-{{ featureType }}">
  //           {% for feature,description in features.items %}
  //             <div class="feature">
  //               <button type="button" class="featureName collapsible">
  //                 {{ feature }}
  //               </button>
  //               <div class="featureDescription collapsing">
  //                 {% for line in description %}
  //                   {% if line.type == "normal" %}
  //                     {% with line.text|split as test %}
  //                       {% for item in test %}
  //                         <p>
  //                           {{ item }}
  //                         </p>
  //                       {% endfor %}
  //                     {% endwith %}
  //                   {% elif line.type == "heading" %}
  //                     <h4>
  //                       {{ line.text }}
  //                     </h4>
  //                   {% elif line.type == "table" %}
  //                     {% with feature|kebab as kebabFeature %}
  //                       {% with line|formatTableJS as formatted %}
  //                         <div id="{{ kebabFeature }}">
  //                         </div>
  //                         <script>inject("{{ kebabFeature }}", "{{ formatted }}")</script>
  //                       {% endwith %}
  //                     {% endwith %}
  //                   {% endif %}
  //                 {% endfor %}
  //               </div>
  //             </div>
  //           {% endfor %}
  //         </div>
  //       {% endfor %}
  //     </section>
  //   </div>
  // )
}
