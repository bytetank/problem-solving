

class MergeSortedArrays{

    constructor(arr1, arr2){
        this.arr1 = arr1;
        this.arr2 = arr2;
        this.merged_array = [];
    }

    merge() {
        let arr1_index = 0;
        let arr2_index = 0;
        while(true){
            if(arr1_index == this.arr1.length){
               for(let j=arr2_index; j < this.arr2.length; j++){
                   this.merged_array.push(this.arr2[j])
               }   
               break  
            }
            if(arr2_index == this.arr2.length){
                for(let k=arr1_index; k < this.arr1.length; k++){
                    this.merged_array.push(this.arr1[k])
                } 
                break
            }
            if(this.arr1[arr1_index] < this.arr2[arr2_index]){
                this.merged_array.push(this.arr1[arr1_index]);
                arr1_index += 1;
            }
            else if (this.arr1[arr1_index] > this.arr2[arr2_index]){
                this.merged_array.push(this.arr2[arr2_index]);
                arr2_index += 1;
            }
            else{
                this.merged_array.push(this.arr1[arr1_index]);
                this.merged_array.push(this.arr2[arr2_index]);
                arr1_index += 1;
                arr2_index += 1;
            }
        }
        return this.merged_array;
    }   
}

const msa = new MergeSortedArrays([0,3,4,5,31], [5,8]);
console.log(msa.merge())