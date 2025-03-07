const images = document.getElementsByClassName('img-item');
const thumbail = document.getElementById("thumbnailImg");
const thumbnailWrapper = document.getElementsByClassName('thumbnail-wrapper')[0];
const leftArrow = document.getElementById("leftArrow");
const rightArrow = document.getElementById("rightArrow");
const callButton = document.getElementsByClassName('call-button')[0];

thumbnailWrapper.disabled = true;
//Event Listeners

[leftArrow,rightArrow].forEach(item =>{
    item.addEventListener("click",changeImage)
})

//Adding event listener for each of the images
for(i =0 ; i < images.length;i++){
    images[i].addEventListener('click',selectImage)
}

//Event listener for the call button
callButton.addEventListener('click',showPhoneNumber);

// On click if phone number is different from our default show the number else show Not provided
function showPhoneNumber(event){
    event.preventDefault();
    phoneNumber = callButton.getAttribute('data-number');
    if(phoneNumber === "00000000000"){
        callButton.innerText= 'Not provided';
        return;
    }
    callButton.innerText= phoneNumber;

}

//On click gets the target src and pass it to the setImage function
function selectImage(event){
    setImage(event.target.src)
}

/*
    I created setImage function rather that invoking setAttribute in both selectImage and Change image
    In this way we don't need to know which function is called all we do is set the src attribute to be the path passed as parameter.


*/
function setImage(path){

    thumbail.setAttribute('src',path)
    
}



/* 
    Change image takes and event for paramater 
    and based on which arrow is pressed increments or decrements the counter variable.
    Which then we use to acces a image from the images array.
    I manage to cover some of the edge cases , but have a lot to test ,yet.

*/
let counter = 0 ;
let index =0;

function changeImage(event){

        if(event.target === rightArrow){
            counter++;
            counter = counter % images.length;
        }

        if(event.target === leftArrow){
            counter--;
            
            if(counter < 0 ){
                counter = images.length -1
            }           
        }
        index = counter ;
        setImage(images[index].src)

   


}