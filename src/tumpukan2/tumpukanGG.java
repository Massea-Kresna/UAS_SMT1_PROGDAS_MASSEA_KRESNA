package tumpukan2;

public class tumpukanGG {
    private node topGanjil;
    private node topGenap;

    public tumpukanGG() {
        topGanjil = null;
        topGenap = null;
    }

    public void push(Integer data) {
        node newNode = new node(data, null);
        if (data % 2 == 0) {
            if (topGenap == null) {
                topGenap = newNode;
            } else {
                newNode.setPtr(topGenap);
                topGenap = newNode;
            }
        } else {
            if (topGanjil == null) {
                topGanjil = newNode;
            } else {
                newNode.setPtr(topGanjil);
                topGanjil = newNode;
            }
        }
    }

    public Object popGanjil() {
        if (topGanjil == null) {
            System.out.println("Tumpukan ganjil kosong.");
            return null;
        } else {
            Object data = topGanjil.getData();
            topGanjil = topGanjil.getPtr();
            return data;
        }
    }

    public Object popGenap() {
        if (topGenap == null) {
            System.out.println("Tumpukan genap kosong.");
            return null;
        } else {
            Object data = topGenap.getData();
            topGenap = topGenap.getPtr();
            return data;
        }
    }

    public void cetakGanjil() {
        if (topGanjil == null) {
            System.out.println("Tumpukan ganjil kosong.");
        } else {
            node current = topGanjil;
            while (current != null) {
                System.out.print(current.getData() + " ");
                current = current.getPtr();
            }
            System.out.println();
        }
    }

    public void cetakGenap() {
        if (topGenap == null) {
            System.out.println("Tumpukan genap kosong.");
        } else {
            node current = topGenap;
            while (current != null) {
                System.out.print(current.getData() + " ");
                current = current.getPtr();
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        tumpukanGG a = new tumpukanGG();

        a.push(10);
        a.push(5);
        a.push(7);
        a.push(3);
        a.push(2);

        System.out.println("=======================");
        System.out.println("Tumpukan Ganjil:");
        a.cetakGanjil();
        System.out.println("Tumpukan Genap:");
        a.cetakGenap();
        System.out.println("=======================");
        System.out.println("Pop Ganjil: " + a.popGanjil());
        System.out.println("Pop Genap: " + a.popGenap());
        System.out.println("=======================");
        System.out.println("Tumpukan Ganjil:");
        a.cetakGanjil();
        System.out.println("Tumpukan Genap:");
        a.cetakGenap();
        System.out.println("=======================");
    }
}
