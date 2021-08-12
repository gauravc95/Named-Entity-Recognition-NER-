<template>
  <div style='padding-left:15%,padding-right:15%'>
    <h1>Named Entity Recognition(NER)</h1>
    <el-card class="box-card" >
    <el-form :model="form" >
      <el-form-item >
        <el-input
          class="input-text"
          type="textarea"
          style="width:900px"
          :rows="9"
          id='textField'
          placeholder="Input text for Entity Recognition"
          v-model="textarea">
        </el-input>
        <el-form-item style="margin-top:20px">
          <el-button @click="extractText" type="primary">Find NER</el-button>
        </el-form-item>
      </el-form-item>

    <div class="tag-group">
      <el-tag class='tag'
        style="margin: 1px 1px 1px 1px"
        v-for="item in entities_color_label"
        :key="item"
        :color = item[1]
        effect="light">
        {{ item[0] }}
      </el-tag>
    </div>

    <div class="tag-group" style='margin-top: 40px'>
    <p class="tooltip" style='margin-top:-30px' v-for="item in items" :key="item.label" v-on:mouseover="showTooltip()">
        {{ item.text }}
        <span class="tooltiptext">{{ item.tag }}</span>
        <el-tag class='tag'
        :key="item.label"
        style="margin: 1px 1px 1px 1px"
        :color = item.color
        effect="light">
        {{ item.label }}
      </el-tag>
    </p>
    </div>
    </el-form>
  </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'firstPage',
  props: {
    msg: String
  },
  data() {
    return {
      textarea: 'In her first remarks since Gov. Andrew M. Cuomo announced his resignation, Lt. Gov. Kathy Hochul, the state’s governor-in-waiting, distanced herself from the embattled governor, while declaring she was prepared to lead New York through economic turmoil and an enduring pandemic.Ms. Hochul stressed she had “not been close” to the governor, saying she was unaware of the conduct outlined in a state attorney general report that found Mr. Cuomo had sexually harassed nearly a dozen women. Ms. Hochul said she would oust Cuomo staffers who acted unethically, signaling she would transform the workplace culture in the governor’s office, which the report had described as hostile and vindictive.At the end of my term, whenever it ends, no one will ever describe my administration as a toxic work environment,Ms. Hochul said in a news conference held at the State Capitol. She is set to be sworn into office on Aug. 24, when Mr. Cuomo’s resignation takes effect',
      items: [],
      entities_color_label:[]
    }
  },
  methods: {
    extractText() {
      axios.post("http://localhost:5000/tests",
        {
          "input_text":this.textarea,
        })
        .then(response => {
          if (this.textarea.length == 0){
              this.$notify({
                title: 'No entities found',
                type: 'Failed',
                message: '',
                duration: 5000
              })
              return
          }
          if (this.textarea.split(/[ ,]+/).length > 500){
              this.$notify({
                title: 'Invalid Input',
                type: 'Failed',
                message: 'Text longer than 500 words',
                duration: 5000
              })
              return
          }
            let extracted_result = response.data.extracted_entity
            let ner_results = []
            const color_code_list = [
              '#ededfb','#B3B31A','#ff7256', '#9900B3', '#4D8066','#1AFF33',
              '#999933','#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
              '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
              '#66664A', '#991AHF', '#E666FA', '#4DB8FF', '#1AB599',
              '#66664B', '#991AGF', '#E666FG', '#4D73FF', '#1AB699',
              '#66664S', '#991AAF', '#E666FS', '#4DB4FF', '#1AB999']

            let pointer = 0
            let color_dict = {}
            let color_label = []

            for (let i=0;i <extracted_result.length;i++){
              if (color_dict[extracted_result[i][2]] == undefined && extracted_result[i][2].length != 0)
              {
                color_dict[extracted_result[i][2]] = color_code_list[pointer]
                color_label.push([extracted_result[i][2],color_code_list[pointer]])
                pointer = pointer+1
              }

              ner_results.push({
                "label":extracted_result[i][0],
                "color":color_dict[extracted_result[i][2]],
                "tag":extracted_result[i][1]
              })
            }
            this.entities_color_label = color_label
            this.items = ner_results
          })
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.card-container {
  margin: auto;
  width: 1500px;
  height: 200px;
  vertical-align: middle;  
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  border: 8px;
}
body {
  padding: 20px;
}
#app {
  width: 100px;
}
.tooltip {
    position: relative;
    display: inline-block;
}
.tag {
  color: black;
  border: black;
  border:2px; 
  height: 35px;
  font-size: large;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    position: absolute;
    z-index: 1;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 1s;
}

.tooltip .tooltiptext::after {
    content: "";
    position: absolute;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
</style>
