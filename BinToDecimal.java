/* ID: 57a5c31ce298a7e6b7000334

Complete the function which converts a binary number (given as a string) to a decimal number. */
package kata;

public class BinToDecimal {

    public static int binToDecimal(String inp) {
        String newInp = "";
        for (int i = 0; i < inp.length(); i++) {
            newInp = inp.charAt(i) + newInp;
        }

        int decimal = 0;
        for (int i = 0; i < newInp.length(); i++) {
            decimal += (newInp.charAt(i) - '0') * Math.pow(2, i);
        }
        return decimal;
    }
}
