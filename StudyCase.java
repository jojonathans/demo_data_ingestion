public class StudyCase{
    public static void main(String[] args) {
        int total = 1;
        for(int i = 0; i<args.length; i++){
            total = total * Integer.parseInt(args[i]);
        }

        if(total %2 == 0){
            System.out.println(String.valueOf(total) + "-Genap");
        } else {
            System.out.println(String.valueOf(total) + "-Ganjil");
        }
        
    }
}
/*
cara compile
javac StudyCase.java -> untuk bilang ke java kemana dia harus liat dir untuk define packagenya
url : https://stackoverflow.com/questions/17408769/how-do-i-resolve-classnotfoundexception
java StudyCase 1 2 3
*/