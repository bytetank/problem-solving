/*
Problem Statement: Implement an array with basic operation like append, pop, get length, access element by index 
*/


class MyArray{
    constructor()
    {
        this.length = 0;
        this.data = {};
    }
    get(index)
    {
        let element_at_index;
        if(this.length > index)
        {
            if(index < 0 )
            {   // can access element with negative index. Last element will have index of -1
                element_at_index = this.data[this.length + index ];
            }
            else
            {
                element_at_index = this.data[index];
            }
        }  
        else
        {
            throw new Error("Index Out of bound");
        }
        console.log(`Get: Element at index ${index} is ${element_at_index}`);
        return element_at_index;
        
    }
    push(element)
    {
        this.data[this.length] = element;
        this.length += 1
        console.log(`Push: New Array after pushing element ${element} is ${JSON.stringify(this.data)}`);
    }

    insert(index, put_element)
    {
         //Insert operation will increase the size of array by one element
        let popped_element;
        for(let i=index; i < this.length; i++){
            try
            {
                popped_element = this.get(i);  //Get the element present in index and store it in variable to move this element to next index
            }
            catch(e)
            {
                console.log(e.message);
                this.push(put_element);
                this.length += 1
                return
            }
            this.data[i] = put_element;
            put_element = popped_element;
        }
        this.data[this.length] = put_element;
        this.length += 1;
        console.log(`Insert: New Array ${JSON.stringify(this.data)}`);
    }
    
    pop(index = this.length - 1){
        // can pop element from any index. Array size wil be reduced by one and array will be adjusted after deleted element
        let put_element;
        for(let i=index; i < this.length-1; i++){   
             this.data[i] = this.get(i+1);  
        }
        delete this.data[this.length-1];
        this.length -= 1 ;
        console.log(`Pop: New Array ${JSON.stringify(this.data)}`)
    }
}



arr = new MyArray();
arr.push("s");
arr.push("w");
arr.push("p");
arr.push("n");
arr.push("i");
arr.push("l");
arr.insert(2,"a");
arr.pop(4);