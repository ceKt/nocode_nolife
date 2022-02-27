
var num2str = function (target){
    if(isNaN(target)){
        console.log("target is not num")
        return
    }
    
    var other_digit = ["thousand","million","billion","trillion","quadrillion"]

    function three_digit2str(t){
        var first_digit_pa = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
        var second_digit = ["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
        var a = ""
        var h = Math.floor(t/100)
        if(10>h && h>0){
            a += first_digit_pa[h] + " hundred "
            t = t%100
        }
        var w = Math.floor(t/10)
        if(10>w && w>1){
            a += second_digit[w] + " "
            t = t%10
        }
        if(20>t){
            a += first_digit_pa[t]
        }
        return a

    }
    function int2str(target){
        var ans = ""
        var qua = Math.floor(target/Math.pow(10,15))
        if(qua>0){
            ans += three_digit2str(qua)+ " " +other_digit[4]+" "
            target = target%Math.pow(10,15)
        }
        var tri = Math.floor(target/Math.pow(10,12))
        if(tri>0){
            ans += three_digit2str(tri)+ " " +other_digit[3]+" "
            target = target%Math.pow(10,12)
        }
        var bil = Math.floor(target/Math.pow(10,9))
        if(bil>0){
            ans += three_digit2str(bil)+ " " +other_digit[2]+" "
            target = target%Math.pow(10,9)
        }
        var mil = Math.floor(target/Math.pow(10,6))
        if(mil>0){
            ans += three_digit2str(mil)+ " " +other_digit[1]+" "
            target = target%Math.pow(10,6)
        }
        var tho = Math.floor(target/Math.pow(10,3))
        if(tho>0){
            ans += three_digit2str(tho)+ " " +other_digit[0]+" "
            target = target%Math.pow(10,3)
        }
        ans += three_digit2str(target)
        return ans
    }
    if(target==0)return "zero"
    if(Number.isInteger(target)){
        var answer = int2str(target)
        return answer
    }
    else{
        var answer = ""
        if(target>1)
            answer += int2str(Math.floor(target)) + " point"
        else
            answer += "zero point"
        var dec = String(target).split(".")[1]
        for(var i = 0; i<dec.length; i++){
            answer += " "+three_digit2str(dec[i])
        }
        return answer
    }
}


if(!module.parent) {
    var input = Number("123456879.123456879")
    console.log(String(input)+"："+num2str(input))
}