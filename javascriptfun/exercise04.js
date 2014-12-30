var myCat = {
    tired: 20,
    hunger: 40,
    lonely: 50,
    happy: 100,
    feed: function(){
        console.log("Om nom nom");
        myCat.hunger = myCat.hunger-5;
        },
    sleep: function(){
        console.log("Zzzzzzz");
        console.log(myCat.tired);
        myCat.tired = myCat.tired-(Math.floor(Math.random()*15));
        console.log(myCat.tired);
                },
    pet: function(){
        console.log("Zzzzzzz");
        myCat.tired = myCat.tired+10;
        },
    laser: function(){
        console.log("EEEEE!!! >.<");
        myCat.tired = myCat.tired-5;
            if (myCat.tired%2===0){
                console.log("Don't pet me! I'm crazy right now!");
            }
        }
};

    

function catStatus(){
    // for (var i=0; i <10; i++){
        console.log(i,":");
        console.log("Hunger:", myCat.hunger);
        console.log("Tired:", myCat.tired);
        console.log("Loneliness:", myCat.lonely);
        console.log("Happiness:", myCat.happy);
    
        myCat.feed();
        myCat.sleep();
        myCat.pet();
        myCat.laser();
    }

catStatus();


function dangerZone(){
    
    if (myCat.hunger <= 20)
        {
            console.log("I'm dying! Meow!");
        }

     if (myCat.hunger < 0)
        {
            console.log("Time to adopt a new cat. I died.");
        }
}