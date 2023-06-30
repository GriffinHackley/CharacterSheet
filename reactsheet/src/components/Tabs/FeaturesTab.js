export default function FeaturesTab({ featuresInfo }) {
  let headers = [];
  let features = [];

  featuresInfo.forEach(element => {
    headers.push(
      <button
        type="button"
        id={element.name + "Button"}
        key={element.name + "Button"}
        className="tabButton"
        data-for-tab={"feature-" + element.name}
      >
        {element.name}
      </button>
    );

    features.push(
      <div class="feature">
        <button type="button" class="featureName collapsible">
          {element.name}
        </button>
        <div class="featureDescription collapsing">
          {/* {% for line in description %}
                      {% if line.type == "normal" %}
                        {% with line.text|split as test %}
                          {% for item in test %}
                            <p>
                              {{ item }}
                            </p>
                          {% endfor %}
                        {% endwith %}
                      {% elif line.type == "heading" %}
                        <h4>
                          {{ line.text }}
                        </h4>
                      {% elif line.type == "table" %}
                        {% with feature|kebab as kebabFeature %}
                          {% with line|formatTableJS as formatted %}
                            <div id="{{ kebabFeature }}">
                            </div>
                            <script>inject("{{ kebabFeature }}", "{{ formatted }}")</script>
                          {% endwith %}
                        {% endwith %}
                      {% endif %}
                    {% endfor %} */}
        </div>
      </div>
    );
  });

  return (
    <div className="tabContent" data-tab="main-features">
      <section className="features">
        <div className="featureHeader tabHeader">
          {headers}
        </div>
      </section>
      <div
        className="featureType tabContent"
        data-tab="feature-{{ featureType }}"
      />
    </div>
  );

  // return (
  //     <div className="tabContent" data-tab="main-features">
  //     <section className="features">
  //       <div className="featureHeader tabHeader">
  //         {% for featureType in character.features %}

  //         {% endfor %}
  //       </div>
  //       {% for featureType,features in character.features.items %}
  //         <div className="featureType tabContent" data-tab="feature-{{ featureType }}">
  //           {% for feature,description in features.items %}
  //             <div className="feature">
  //               <button type="button" className="featureName collapsible">
  //                 {{ feature }}
  //               </button>
  //               <div className="featureDescription collapsing">
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
