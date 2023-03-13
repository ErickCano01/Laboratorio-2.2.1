/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package scrum;

/**
 *
 * @author galindo
 */
public class SCRUM {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Proyecto proyecto = new Proyecto("Proyecto 1", "20-19-2023", true);
        
        Stakeholder guillermo = new Stakeholder(100, "memo", 0);
        proyecto.stakeholders.add(guillermo);
        
        ScrumMaster pepe = new ScrumMaster("pepe");
        Equipo equipo = new Equipo("Bum Bum", 0, pepe);
        
        Integrante juan = new Integrante("Juan", "Diseñador");
        equipo.integrantes.add(juan);
        
        Integrante leo = new Integrante("Leo", "Analista");
        equipo.integrantes.add(leo);
        
        proyecto.equipos.add(equipo);
        
        System.out.println(proyecto);
    }
    
}
