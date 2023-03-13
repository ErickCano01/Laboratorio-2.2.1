package scrum;

import java.util.Vector;

public class Integrante {

    private String nombre;
    private String rol;
    public Vector<Tareas> tareas = new Vector<Tareas>();

    public Integrante(String nombre, String rol) {
        this.nombre = nombre;
        this.rol = rol;
    }
    
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String aNombre) {
        this.nombre = aNombre;
    }

    public String getRol() {
        return this.rol;
    }

    public void setRol(String aRol) {
        this.rol = aRol;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Integrante{");
        sb.append("nombre=").append(nombre);
        sb.append(", rol=").append(rol);
        sb.append(", tareas=").append(tareas);
        sb.append('}');
        return sb.toString();
    }

}
