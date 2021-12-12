class Card extends Payment {
    constructor(id, cardNumber, cardDate, cvv) {
        //? "super" makes reference to atributes and methods of the super class or father class
        super(id);
        //? While "this" makes reference to the class you are right know or the child class
        this.cardNumber = cardNumber;
        this.cardDate = cardDate;
        this.cvv = cvv;
    }
}
