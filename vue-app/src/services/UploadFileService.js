import http from "../http-common"

class UploadFileService{
    upload(file, onUploadProgress, selection, type, node) {
        if(node === undefined){
            alert("Select Filter");
        }
        else{
        let formData = new FormData();

        formData.append("file", file);
        formData.append("selection", selection);
        formData.append("type", type);
        return http.post("/upload", formData, {
        headers: {
            "Content-Type": "multipart/form-data"
        },
        onUploadProgress
        }); 
    }
    }

    getFiles() {
        return http.get("/analysis")
    }
}
export default new UploadFileService();