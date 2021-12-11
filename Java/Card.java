package Java;

public class Card extends Payment {
    Integer cardNumber;
    String cardDate;
    String cvv;

    public Card(Integer id,Integer cardNumber, String cardDate, String cvv){
        super(id);
        this.cardNumber = cardNumber;
        this.cardDate = cardDate;
        this.cvv = cvv;
    }
}
