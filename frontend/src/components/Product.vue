<!-- <template>
    <div class="hello">
     <h1>We here</h1>
    </div>
  </template> -->

  <template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Products</h1>
          <hr><br><br>
        
          <!-- <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Product</button> -->
          
          <br><br>
          <h6>Total Products: {{ total }}</h6>
          <br><br>
          <table class="table table-hover">
            <thead> 
              <tr>
                <th scope="col">Product Number</th>
                <th scope="col">Product Name</th>
                <th scope="col">Product Owner</th>
                <th scope="col">Developer Names</th>
                <th scope="col">Scrum Master</th>
                <th scope="col">Start Date</th>
                <th scope="col">Methodology</th>

                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index">
                <td>{{ product.product_id }}</td>
                <td>{{ product.productName }}</td>
                <td>{{ product.productOwnerName }}</td>
                <td>{{ product.Developers.toString() }}</td>      
                <!-- <td v-for = "(developer,index2) in product.Developers" :key="index2">
                    
                        <li>{{ developer }}</li>
                
                </td> -->
                <td>{{ product.scrumMasterName }}</td>         
                <td>{{ product.startDate }}</td>
                <td>{{ product.methodology }}</td>
                <td>
                  <!-- <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div> -->
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  
import axios from 'axios';

  export default {

    name: 'ProductIbm',
    data() {
        return {
            products :[],
            total : 0, 
           
            
           
        };
    },
    
    methods : {
        getProducts() {
            const path = 'http://localhost:3000/api/products/';
            axios.get(path)
                .then((res) => {
    
                    this.products = res.data.products;
                    this.total = this.products.length;
                   
                }).catch((error)=>{
                    console.log(error);
                });

        },
       
    },
    components: {
   
  },
    
  
    created() {
        this.getProducts();
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h1 {
    margin: 40px 0 0;
  }
  </style>
  