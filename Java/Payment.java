package Java;

class Payment {
    Integer id;

    public Payment(Integer id) {
        this.id = id;
    }

    protected void printPaymentData() {
        System.out.println("id: " + id);
    }
}
