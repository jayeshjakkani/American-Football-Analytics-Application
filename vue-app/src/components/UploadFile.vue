<template>
<div>
    

    <label class="btn btn-default">
      <input type="file" multiple @change="selectFile" />
    </label>

    <button class="btn btn-success"
      :disabled="!selectedFiles"
      @click="uploadFiles"
    >
      upload
    </button>
    <treeselect name="testVar" v-model="value" :multiple="false" :options="options" v-on:select="selected"
        :disable-branch-nodes="true" placeholder="Please Select a FILTER option"
    />
    <div v-if="message" class="alert alert-light" role="alert">
      <ul>
        <li v-for="(ms, i) in message.split('\n')" :key="i">
          {{ ms }}
        </li>
      </ul>
    </div>

    
  </div>
</template>
<script>
import { bus } from "@/event-bus";
import UploadService from "../services/UploadFileService";
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
export default {
  name: "upload-files",
  components: { Treeselect },
  data() {
    return {
      selectedFiles: undefined,
      currentFile: undefined,
      progress: 0,
      message: "",
      fileInfos: [],
       
        value: null,
    
        options: [ {
          id: 'NO FILTER',
          label: 'NO FILTER',
        },{  
          id: 'Season',
          label: 'Season',
          children: [ {
            id: '2019',
            type: 'Season',
            label: '2019',
          }, {
            id: '2018',
            type: 'Season',
            label: '2018',
          },{
            id: '2017',
            type: 'Season',
            label: '2017',
          },{
            id: '2016',
            type: 'Season',
            label: '2016',
              } ],
        }, 
         {
          id: 'Month',
          label: 'Month',
          children: [ {
            id: '1',
            type: 'Month',
            label: '1',
          }, {
            id: '2',
            type: 'Month',
            label: '2',
          },{
            id: '3',
            type: 'Month',
            label: '3',
          },{
            id: '4',
            type: 'Month',
            label: '4',
              },{
            id: '5',
            type: 'Month',
            label: '5',
          }, {
            id: '6',
            type: 'Month',
            label: '6',
          },{
            id: '7',
            type: 'Month',
            label: '7',
          },{
            id: '8',
            type: 'Month',
            label: '8',
            }, {
            id: '9',
            type: 'Month',
            label: '9',
          }, {
            id: '10',
            type: 'Month',
            label: '10',
          },{
            id: '11',
            type: 'Month',
            label: '11',
          },{
            id: '12',
            type: 'Month',
            label: '12',
            } ],
        },
        {
          id: 'Week',
          label: 'Week',
          children: [ {
            id: '1',
            type: 'Week',
            label: '1',
          }, {
            id: '2',
            type: 'Week',
            label: '2',
          },{
            id: '3',
            type: 'Week',
            label: '3',
          },{
            id: '4',
            type: 'Week',
            label: '4',
              },{
            id: '5',
            type: 'Week',
            label: '5',
          }, {
            id: '6',
            type: 'Week',
            label: '6',
          },{
            id: '7',
            type: 'Week',
            label: '7',
          },{
            id: '14',
            type: 'Week',
            label: '14',
          }],
      },{
          id: 'Match',
          label: 'Match',
          children: [ {
            id: '15720',
            type: 'Match',
            label: '15720',
          }, {
            id: '8293',
            type: 'Match',
            label: '8293',
          },{
            id: '8384',
            type: 'Match',
            label: '8384',
          },{
            id: '12470',
            type: 'Match',
            label: '12470',
              },{
            id: '12150',
            type: 'Match',
            label: '12150',
          }],
      },{
          id: 'Opponent',
          label: 'Opponent',
          children: [ {
            id: 'NCUN',
            type: 'Opponent',
            label: 'NCUN',
          }, {
            id: 'SCUN',
            type: 'Opponent',
            label: 'SCUN',
          },{
            id: 'WVMA',
            type: 'Opponent',
            label: 'WVMA',
          },{
            id: 'VAUN',
            type: 'Opponent',
            label: 'VAUN',
              },{
            id: 'VAJN',
            type: 'Opponent',
            label: 'VAJN',
          }],
        }],
    };
  },
  methods: {
    selectFile() {
      this.progressInfos = [];
      this.selectedFiles = event.target.files;
    },
    selected(node) {
        console.log(node);
        this.node = node;
        this.selection = node.label;
        this.type = node.type;
    },
    uploadFiles() {
      this.message = "";

      for (let i = 0; i < this.selectedFiles.length; i++) {
        this.upload(i, this.selectedFiles[i]);
      }
    },
    upload(idx, file) {
      this.progressInfos[idx] = { percentage: 0, fileName: file.name };

      UploadService.upload(file, (event) => {
        this.progressInfos[idx].percentage = Math.round(100 * event.loaded / event.total);
      }, this.selection, this.type, this.node)
        .then((response) => {
          console.log("Success!");
          bus.$emit("upload-success");
          console.log(response.data);
        })
        .catch(() => {
          this.progressInfos[idx].percentage = 0;
          this.message = "Could not upload the file:" + file.name;
        });
    }
  },
  mounted() {
    UploadService.getFiles().then(response => {
      this.fileInfos = response.data;
    });
  }
};
</script>
<style scoped>
.column {
  width: 100px;
}
</style>

